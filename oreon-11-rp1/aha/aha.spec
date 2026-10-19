%global source0_hash 6aea13487f6b5c3e453a447a67345f8095282f5acd97344466816b05ebd0b3b1
Name: aha
Summary:        Convert terminal output to HTML
License: MPL-1.1 OR LGPL-2.0-or-later
Version: 0.5.1
Release:        1%{?dist}
URL: https://github.com/theZiz/aha
Source0:        https://github.com/theZiz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: 0000-fix-null-pointer-dereference.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
%{name} parses output from other programs,
recognizes ANSI terminal escape sequences
and produces an HTML rendition of the original text.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Extract license header from source code
cat aha.c | awk '1;/\*\//{exit}' > LICENSE

%build

%set_build_flags
%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
