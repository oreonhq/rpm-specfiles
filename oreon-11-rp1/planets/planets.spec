%global source0_hash cd4be19dc1e16cc3d5bb20fdfa2af025b50cd21dbce5d1e8b3041c4e786c3624

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name: planets
Version:  0.1.13
Release:  51%{?dist}
Summary: A celestial simulator  

License: GPL-2.0-or-later
URL: http://planets.homedns.org/
Source0: http://planets.homedns.org/dist/planets-%{version}.tgz
# Adapt to changes in OCaml 4.x
Patch0:  planets-0.1.13-ocaml4.patch
# Fix for immutable strings.  NOT sent upstream (because upstream
# is not alive?)
Patch1:  planets-0.1.13-bytes.patch
# Use camlp5 instead of the dead camlp4 package
Patch2:  planets-0.1.13-camlp5o.patch
# Generate usable debuginfo
Patch3:  planets-0.1.13-debuginfo.patch
# Adapt to changes in OCaml 5.x
Patch4:  planets-0.1.13-ocaml5.patch
# Adapt to changed unix library name in OCaml 5.1.0
Patch5:  planets-0.1.13-ocaml5.1.patch
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: ocaml-camlp-streams-devel
BuildRequires: ocaml-camlp5-devel
BuildRequires: ocaml-labltk-devel
Requires: hicolor-icon-theme

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%description
Planets is a simple interactive program for playing with simulations
of planetary systems

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

iconv -f ISO-8859-1 -t UTF-8 TODO > iconv.tmp
mv iconv.tmp TODO

%ifarch %{ocaml_native_compiler}
make
%else
make planets.bc
%endif

%install
mkdir -p  %{buildroot}%{_bindir}
%ifarch %{ocaml_native_compiler}
install -m 755 planets %{buildroot}%{_bindir}/planets
%else
install -m 755 planets.bc %{buildroot}%{_bindir}/planets
%endif
mkdir -p %{buildroot}%{_mandir}/man1
cp -pr planets.1 %{buildroot}%{_mandir}/man1

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --remove-category Application               \
  --add-category Simulation                  \
  --dir %{buildroot}%{_datadir}/applications \
  planets.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 planets.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%doc CHANGES codeguide.txt CREDITS getting_started.html KEYBINDINGS.txt README TODO VERSION
%license COPYING LICENSE
%{_bindir}/planets
%{_datadir}/applications/planets.desktop
%{_datadir}/icons/hicolor/32x32/apps/planets.png
%{_mandir}/man1/planets.1.gz

%changelog
%autochangelog
