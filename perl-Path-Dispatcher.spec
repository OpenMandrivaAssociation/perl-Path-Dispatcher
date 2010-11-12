%define upstream_name    Path-Dispatcher
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    All rules must match
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Path/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Try::Tiny)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
We really like the Jifty::Dispatcher manpage and wanted to use it for the
Prophet manpage's command line.

The basic operation is that of dispatch. Dispatch takes a path and a list
of rules, and it returns a list of matches. From there you can "run" the
rules that matched. These phases are distinct so that, if you need to, you
can inspect which rules were matched without ever running their codeblocks.

You want to use the Path::Dispatcher::Declarative manpage which gives you
some sugar inspired by the Jifty::Dispatcher manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/Path/


