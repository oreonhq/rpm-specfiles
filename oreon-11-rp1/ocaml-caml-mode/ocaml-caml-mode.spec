%global source1_hash ba5b3bec59d5ba665c651447af4ca7da019ad4ad8c032f7a1d48c997a54fd11a
%global source0_hash f74d2bfd696618d2699d0cad378079a1014f939293250bacb6763b089e430d7a
%global srcname caml-mode
%global debug_package %{nil}
Name:           ocaml-%{srcname}
Version:        4.9
Release:        12%{?dist}
Summary:        Opam file for caml-mode
License:        GPL-2.0-or-later AND GPL-1.0-or-later
URL:            https://github.com/ocaml/caml-mode
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml/%{srcname}/releases/download/%{version}/%{srcname}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/ocaml/opam-repository/master/packages/%{srcname}/%{srcname}.%{version}/opam
Requires:       emacs-%{srcname} = %{version}-%{release}
Requires:       ocaml(runtime)
# oreon:deps
BuildRequires:  emacs-nw
BuildRequires:  make
# /oreon:deps
%description
This package contains the opam file for emacs-%{srcname}.  Install this only
if you want opam to know that caml-mode is available.  If you just want to use
caml-mode, install emacs-%{srcname}.

%package     -n emacs-%{srcname}
Summary:        Emacs mode for editing OCaml source code
BuildArch:      noarch
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
%description -n emacs-%{srcname}
This package provides a caml-mode for Emacs, for editing OCaml programs, as
well as an inferior-caml-mode, to run a toplevel.  Caml-mode supports
indentation, compilation and error retrieving, and sending phrases to the
toplevel.  There is also support for hilit, font-lock and imenu.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%make_build ocamltags
%install
export INSTALL_BIN=%{buildroot}%{_bindir}
export INSTALL_DIR=%{buildroot}%{_emacs_sitelispdir}/%{srcname}
mkdir -p %{buildroot}%{_bindir}
make install install-ocamltags
mkdir -p %{buildroot}%{ocamldir}/%{srcname}
sed '/opam-version/aname: "caml-mode"\nversion: "%{version}"' %{SOURCE1} > \
  %{buildroot}%{ocamldir}/%{srcname}/opam
touch -r %{SOURCE1} %{buildroot}%{ocamldir}/%{srcname}/opam
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cd %{buildroot}%{_emacs_sitelispdir}/%{srcname}
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"%{buildroot}%{_emacs_sitestartdir}/caml-mode-loaddefs.el\"))"
cd -
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n emacs-caml-mode -f %{oreon_filedir}/emacs-caml-mode.list

%changelog

%autochangelog
