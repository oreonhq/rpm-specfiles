%global source0_hash 2d6bb5583f0b1a1a9825b0de1e836482f07af44484c2d73c5ad9472bdfa2fba1
Name:           hexer
Version:        1.0.7
Release:        1%{?dist}
Summary:        Interactive binary editor
License:        BSD-2-Clause AND BSD-3-Clause
URL:            http://devel.ringlet.net/editors/hexer/
Source0:        http://devel.ringlet.net/files/editors/hexer/hexer-%{version}.tar.xz
Patch0:         0000-sighandler.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Hexer is an interactive binary editor (also known as a hex-editor)
with a Vi-like interface. Its most important features are multiple buffers,
multiple-level undo, command-line editing with completion, and binary regular
expressions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build PREFIX=%{_prefix}
%install
mkdir -p %{buildroot}%{_bindir}/
cp -p hexer %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p hexer.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
