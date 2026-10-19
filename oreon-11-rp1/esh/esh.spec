%global source0_hash 4103b8901c7346f5dd608f2aa272d23c259434f825e6f39b2fb642157d6a2a7c
Name:           esh
Version:        0.3.2
Release:        1%{?dist}
Summary:        Simple templating engine based on shell
License:        MIT
URL:            https://github.com/jirutka/esh
Source0:        https://github.com/jirutka/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       /usr/bin/awk
Requires:       /usr/bin/sed
# oreon:deps
BuildRequires:  /usr/bin/asciidoctor
BuildRequires:  /usr/bin/make
# /oreon:deps
%description
esh (embedded shell) is a templating engine for evaluating shell commands
embedded in arbitrary templates. It’s like ERB (Embedded RuBy) for shell,
intended to be used for templating configuration files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install prefix=%{_prefix}
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
