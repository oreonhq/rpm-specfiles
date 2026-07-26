%global source0_hash e2797c85a2b617b2b35024566105f4d8e998ef576f0f96f7923abf3717d12e86

Name:           qmic
Version:        1.0
Release:        %autorelease
Summary:        QMI IDL compiler

License:        BSD-3-Clause
URL:            https://github.com/andersson/qmic

Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
QMI IDL compiler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build prefix="%{_prefix}"

%install
%make_install prefix="%{_prefix}"

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
