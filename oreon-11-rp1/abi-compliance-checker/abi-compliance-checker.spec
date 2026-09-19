%global source0_hash b1e32a484211ec05d7f265ab4d2c1c52dcdb610708cb3f74d8aaeb7fe9685d64

Name:           abi-compliance-checker
Version:        2.3
Release:        21%{?dist}
Summary:        An ABI Compliance Checker

License:        LGPL-2.1-or-later
URL:            http://lvc.github.io/abi-compliance-checker/
Source0:        https://github.com/lvc/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
Requires:       gcc >= 4.5
Requires:       gcc-c++ >= 4.5
Requires:       binutils
Requires:       findutils
Requires:       ctags >= 5.8
Requires:       abi-dumper >= 0.99.15

Conflicts:      ccache < 3.1.2

%{?perl_default_filter}

%description
A tool for checking backward binary compatibility of a shared C/C++ library. It
checks for changes in calling stack, changes in v-table, removed symbols, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}
%{_fixperms} %{buildroot}/*

%files
%license LICENSE
%doc README.md doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
