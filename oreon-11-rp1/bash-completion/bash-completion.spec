%global source0_hash dd9d825e496435fb3beba3ae7bea9f77e821e894667d07431d1d4c8c570b9e58
%bcond_with tests
%global _python_bytecompile_errors_terminate_build 0
%define upstream_version 2.17.0
Name:           bash-completion
Version:        2.18.0
Release:        1%{?dist}
Epoch:          1
Summary:        Programmable completion for Bash
License:        GPL-2.0-or-later
URL:            https://github.com/scop/bash-completion
Source0:        https://github.com/scop/%{name}/releases/download/%{upstream_version}/%{name}-%{upstream_version}.tar.xz
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       bash >= 4.1
# oreon:deps
BuildRequires:  automake
BuildRequires:  dejagnu
BuildRequires:  make
BuildRequires:  screen
BuildRequires:  tcllib
# /oreon:deps
%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash.

%package devel
Summary: Development files for %{name}
Requires: %{name} =  %{epoch}:%{version}-%{release}
%description devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{upstream_version} -p1

%build

autoreconf -fi -v
%configure
%make_build
%install
%make_install
rm %{buildroot}%{_datadir}/bash-completion/completions/{cowsay,cowthink}
rm %{buildroot}%{_datadir}/bash-completion/completions/makepkg
rm %{buildroot}%{_datadir}/bash-completion/completions/prelink
rm %{buildroot}%{_datadir}/bash-completion/completions/javaws
rm %{buildroot}%{_datadir}/bash-completion/completions/interdiff
%oreon_autofiles bash-completion-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LANG=C.UTF-8
%if %{with tests}
tmpfile=$(mktemp)
screen -D -m sh -c '( make check ; echo $? ) >'$tmpfile
cat $tmpfile
result=$(tail -n 1 $tmpfile)
rm -f $tmpfile
exit $result
%else
make -C completions check
%endif
%files -f %{oreon_filedir}/main.list
%files -n bash-completion-devel -f %{oreon_filedir}/bash-completion-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17-2
- Prepare for Oreon 11 (RP1)
