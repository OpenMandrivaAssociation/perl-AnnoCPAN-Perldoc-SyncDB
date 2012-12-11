%define upstream_name    AnnoCPAN-Perldoc-SyncDB
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Download the AnnoCPAN database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/AnnoCPAN/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
This module provides a simple interface to mirror the the
http://annocpan.org/ manpage content to a local machine. In conjunction
with the the AnnoCPAN::Perldoc manpage module, this allows one to get all
the benefits of the AnnoCPAN website in one's local 'perldoc' command.

Recommended usage: 1) Install this module and AnnoCPAN::Perldoc, 2) set up
a weekly process to run the 'syncannopod' command included in this
distribution, 3) Put the following in your shell configuration: 'alias
perldoc annopod'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog LICENSE README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/syncannopod


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 654873
- rebuild for updated spec-helper

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 503920
- rebuild using %%perl_convert_version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11-2mdv2010.0
+ Revision: 376127
- fixing man1 %%files
- rebuild

* Tue Mar 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11-1mdv2009.1
+ Revision: 362914
- import perl-AnnoCPAN-Perldoc-SyncDB


* Tue Mar 31 2009 cpan2dist 0.11-1mdv
- initial mdv release, generated with cpan2dist

