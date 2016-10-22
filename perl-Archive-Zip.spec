%{?scl:%scl_package perl-Archive-Zip}

Name:           %{?scl_prefix}perl-Archive-Zip
Version:        1.59
Release:        1%{?dist}
Summary:        Perl library for accessing Zip archives

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Archive-Zip/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PH/PHRED/Archive-Zip-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
%if %{defined perl_small}
BuildRequires:  sed
%endif
# Run-time
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Compress::Raw::Zlib)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.80
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(integer)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::Seekable)
BuildRequires:  %{?scl_prefix}perl(Time::Local)
BuildRequires:  %{?scl_prefix}perl(vars)
# Tests
BuildRequires:  %{?scl_prefix}perl(File::Spec::Unix)
# IO::Scalar not used
BuildRequires:  %{?scl_prefix}perl(lib)
%if !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::MockModule)
%endif
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  unzip
BuildRequires:  zip
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Exporter)
Requires:       %{?scl_prefix}perl(File::Spec) >= 0.80

# Remove under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(File::Spec)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(File::Spec\\)$
%endif

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.
Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.
Members can be added, removed, extracted, replaced, rearranged, and
enumerated.  They can also be renamed or have their dates, comments,
or other attributes queried or modified.  Their data can be compressed
or uncompressed as needed.  Members can be created from members in
existing Zip files, or from existing directories, files, or strings.


%prep
%setup -q -n Archive-Zip-%{version}
%{?scl:scl enable %{scl} '}perl -MConfig -pi -e %{?scl:'"}'%{?scl:"'}s|^#!/usr/local/bin/perl|$Config{startperl}|%{?scl:'"}'%{?scl:"'} \
    examples/selfex.pl%{?scl:'}
for F in examples/*.pl; do
    %{?scl:scl enable %{scl} '}perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(q{%{?scl:'"}$F%{?scl:"'}})"%{?scl:'}
done
%if %{defined perl_small}
rm t/23_closed_handle.t
sed -i -e '/^t\/23_closed_handle.t/d' MANIFEST
%endif


%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}


%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}


%files
%doc Changes examples/
%{_bindir}/crc32
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive*.3*


%changelog
* Mon Aug 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.59-1
- 1.59 bump

* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 1.57-3
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.57-2
- Perl 5.24 rebuild

* Mon Apr 04 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.57-1
- 1.57 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.56-1
- 1.56 bump

* Mon Dec 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.55-1
- 1.55 bump

* Fri Sep 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.53-1
- 1.53 bump

* Tue Sep 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-1
- 1.51 bump

* Wed Aug 26 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.50-1
- 1.50 bump

* Mon Aug 03 2015 Petr Pisar <ppisar@redhat.com> - 1.49-1
- 1.49 bump

* Fri Jun 19 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-1
- 1.48 bump

* Thu Jun 18 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.47-1
- 1.47 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-2
- Perl 5.22 rebuild

* Wed Mar 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.46-1
- 1.46 bump

* Tue Feb 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-1
- 1.45 bump

* Thu Jan 15 2015 Petr Pisar <ppisar@redhat.com> - 1.39-2
- Correct dependencies
- Improve sharpbang fix

* Wed Oct 22 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-1
- 1.39 bump

* Wed Sep 10 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-1
- 1.38 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-1
- 1.37 bump

* Thu Jan 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-1
- 1.36 bump

* Tue Dec 10 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-1
- 1.34 bump

* Fri Nov 22 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-1
- 1.33 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.30-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.30-9
- Perl 5.16 rebuild
- Specify all dependencies

* Mon Mar 19 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.30-8
- 543660 apply patch from rt cpan 54827

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.30-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.30-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.30-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.30-2
- rebuild against perl 5.10.1

* Mon Jul 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.30-1
- update to 1.30

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 1.23-1
- Update to 1.23.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-5
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-4
- rebuild for new perl

* Thu Aug 23 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-3
- Fix license tag

* Wed Jun 27 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-2
- Resolves: rhbz#226240
- Incorporate changes from Steven Pritchard's package review
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Remove check macro cruft.
- Update build dependencies.
- Package LICENSE.
- BR unzip, zip for better test coverage.

* Tue Jun 05 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-1
- Update to latest CPAN version: 1.20
- Fix broken changelog

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.16-1.2.1
- rebuild

* Fri Feb 03 2006 Jason Vas Dias<jvdias@redhat.com> - 1.16-1.2
- rebuilt for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Mon Jul 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.16-1
- Update to 1.16.

* Thu Apr 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Aug 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.12-0.fdr.1
- Update to 1.12.

* Tue Jul  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.11-0.fdr.1
- Update to 1.11.
- Bring up to date with current fedora.us Perl spec template.

* Sun Apr 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.10-0.fdr.1
- Update to 1.10.
- Reduce directory ownership bloat.
- Require perl(:MODULE_COMPAT_*).

* Fri Nov 28 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.09-0.fdr.1
- Update to 1.09.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.08-0.fdr.1
- Update to 1.08.

* Tue Oct 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.07-0.fdr.1
- Update to 1.07.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.06-0.fdr.1
- Update to 1.06.
- Specfile cleanups.

* Sun Jun  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.05-0.fdr.1
- First build.
