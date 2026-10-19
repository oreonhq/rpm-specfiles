%global source0_hash 87b3e40584730d6f8b8cdb9deb1700173d25dc54403fcb17d2c1d9def2ba8102
Name:           jo
Summary:        Small utility to create JSON objects
Version:        1.9
Release:        1%{?dist}
URL:            https://github.com/jpmens/jo
Source0:        https://github.com/jpmens/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License:        GPL-2.0-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
Patch:          %{url}/pull/216.patch
Patch:          %{url}/pull/217.patch
ExcludeArch:    %{ix86}
%if !0%{?el10}
%endif
Provides:       bundled(ccan-json) = 0.1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pandoc
BuildRequires:  pkgconfig(bash-completion)
# /oreon:deps
%description
This is jo, a small utility to create JSON objects

  $ jo -p name=jo n=17 parser=false
  {
      "name": "jo",
      "n": 17,
      "parser": false
  }

or arrays

  $ seq 1 10 | jo -a
  [1,2,3,4,5,6,7,8,9,10]

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%meson

%build

%meson_build
%install
%meson_install
install -D -p -m 0644 jo.zsh '%{buildroot}%{zsh_completions_dir}/_jo'
%oreon_autofiles main

%check

ln -s '%{buildroot}%{_bindir}/jo' .
bash -e ./tests/jo.test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
