%global source0_hash aa7a52bf913ab1a64743551d64575f921df3faa4a592a0f6614e047bc228708a

Name:           abi-dumper
Version:        1.4
Release:        5%{?dist}
Summary:        Tool to dump ABI of an ELF object containing DWARF debug info

License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            http://github.com/lvc/abi-dumper/
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  sed
BuildRequires:  txt2man

Requires:       elfutils
Requires:       vtable-dumper >= 1.1

%{?perl_default_filter}

%description
A tool to dump ABI of an ELF object containing DWARF debug info.

The tool is intended to be used with ABI Compliance Checker tool for tracking
ABI changes of a C/C++ library or kernel module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_prefix}
%{__perl} Makefile.pl -install --prefix=%{buildroot}%{_prefix}

chmod 0755 %{buildroot}%{_bindir}/%{name}

# Create manpage
mkdir -p %{buildroot}%{_mandir}/man1
%{__perl} abi-dumper.pl --help | sed "s|:$||g" | \
  txt2man -t ABI-DUMPER -s 1 -v "User Commands" -r "ABI Dumper %{version}" > \
  %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
