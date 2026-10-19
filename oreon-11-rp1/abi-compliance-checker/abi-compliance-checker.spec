%global source0_hash b1e32a484211ec05d7f265ab4d2c1c52dcdb610708cb3f74d8aaeb7fe9685d64
Name:           abi-compliance-checker
Version:        2.3
Release:        21%{?dist}
Summary:        An ABI Compliance Checker
License:        LGPL-2.1-or-later
URL:            http://lvc.github.io/abi-compliance-checker/
Source0:        https://github.com/lvc/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       gcc >= 4.5
Requires:       gcc-c++ >= 4.5
Requires:       binutils
Requires:       findutils
Requires:       ctags >= 5.8
Requires:       abi-dumper >= 0.99.15
Conflicts:      ccache < 3.1.2
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A tool for checking backward binary compatibility of a shared C/C++ library. It
checks for changes in calling stack, changes in v-table, removed symbols, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
