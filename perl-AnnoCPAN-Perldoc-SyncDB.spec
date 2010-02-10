%define upstream_name    AnnoCPAN-Perldoc-SyncDB
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Download the AnnoCPAN database
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/AnnoCPAN/%{upstream_name}-%{upstream_version}.tgz

BuildRequires: perl(File::Spec)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/syncannopod
