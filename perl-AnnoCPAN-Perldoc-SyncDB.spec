%define upstream_name    AnnoCPAN-Perldoc-SyncDB
%define upstream_version 0.11
Name:		perl-%{upstream_name}
Version:	0.11
Release:	2

Summary:	Download the AnnoCPAN database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/AnnoCPAN-Perldoc-SyncDB
Source0:	https://cpan.metacpan.org/authors/id/C/CL/CLOTHO/AnnoCPAN-Perldoc-SyncDB-0.11.tgz

BuildRequires:	make
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
%setup -q -n AnnoCPAN-Perldoc-SyncDB-0.11

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc ChangeLog LICENSE README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/syncannopod


