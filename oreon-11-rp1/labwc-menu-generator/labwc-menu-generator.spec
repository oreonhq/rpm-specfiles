%global source0_hash 4c31e268579b943388dff31f5f5296496dfa0679a15eefdd3a8f8fe2c41a3f89

Name:           labwc-menu-generator
Version:        0.1.0
Release:        5%{?dist}
Summary:        Menu generator for labwc

# Tests are GPL-2.0-or-later
SourceLicense:  GPL-2.0-only AND GPL-2.0-or-later
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc-menu-generator
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  /usr/bin/prove
BuildRequires:  scdoc
Supplements:    labwc

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/labwc-menu-generator.1.gz

%changelog
%autochangelog
