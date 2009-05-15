
%define realname   AnnoCPAN-Perldoc-SyncDB
%define version    0.11
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Download the AnnoCPAN database
Source:     http://www.cpan.org/modules/by-module/AnnoCPAN/%{realname}-%{version}.tgz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(File::Spec)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/syncannopod
/usr/share/man/man1/syncannopod.1.lzma

