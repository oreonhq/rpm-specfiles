%global source0_hash 53c51d656801fd3ae0179a5b27f028e07eaba328e80c8c55050268359b9a2924
%global debug_package	%{nil}
Name:		e3
Version:	2.82
Release:        1%{?dist}
Summary:        Text editor with key bindings similar to WordStar, Emacs, pico, nedit, or vi
License:	GPL-2.0-only
URL:		https://sites.google.com/site/e3editor/
Source0:        https://sites.google.com/site/e3editor/Home/%{name}-%{version}.tgz
Patch0:		e3-gnu-stack.patch
ExclusiveArch:	%{ix86} x86_64
# oreon:deps
BuildRequires:  make
BuildRequires:  nasm
# /oreon:deps
%description
e3 is a full-screen, user-friendly text editor with an key bindings similar to
that of either WordStar, Emacs, pico, nedit, or vi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# delete the included binaries
rm -rf bin

%patch -P0 -p1

%build

%ifarch x86_64
make PREFIX=%{_prefix} MANDIR=%{_mandir}/man1 EXMODE=SED 64
%else
make PREFIX=%{_prefix} MANDIR=%{_mandir}/man1 EXMODE=SED 32
%endif
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 e3 %{buildroot}%{_bindir}
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3ws
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3em
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3pi
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3vi
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3ne
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 e3.man %{buildroot}%{_mandir}/man1/e3.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3ws.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3em.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3pi.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3vi.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3ne.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
