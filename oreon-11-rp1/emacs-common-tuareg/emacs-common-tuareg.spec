%global source0_hash b9507678ba83048f3c5e53256cb47f9d4bf94d587711aa7aeb14cd86bb81df68

%global pkg tuareg
%global pkgname Tuareg-mode

# If the emacs-el package has installed a pkgconfig file, use that to
# determine install locations and Emacs version at build time,
# otherwise set defaults.
%if %($(pkg-config emacs) ; echo $?)
%global emacs_version 28.2
%global emacs_lispdir %{_datadir}/emacs/site-lisp
%global emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%global emacs_version %(pkg-config emacs --modversion)
%global emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%global emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif

Name:           emacs-common-%{pkg}
Version:        3.0.1
Release:        14%{?dist}
Summary:        Emacs mode for editing OCaml code

License:        GPL-2.0-or-later
URL:            https://github.com/ocaml/%{pkg}
Source0:        https://github.com/ocaml/tuareg/archive/%{version}/tuareg-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs, emacs-el
BuildRequires:  emacs-caml-mode
BuildRequires:  emacs-merlin
BuildRequires:  make

# Needs caml-types.el in order to use *.annot files properly.
Recommends:     emacs-caml-mode
Recommends:     emacs-merlin

%description
Tuareg is an OCaml mode for GNU Emacs.  It handles automatic indentation
of Objective Caml and Caml Light code.  Key parts of the code are
highlighted using Font-Lock.  Support to run an interactive Caml
toplevel and debbuger is provided.

This package contains the common files.  Install emacs-%{pkg} to get
the complete package.

%package -n emacs-%{pkg}
Summary:        Compiled elisp files to run %{pkgname} under GNU Emacs
Requires:       emacs(bin) >= %{emacs_version}
Requires:       emacs-common-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg}
Tuareg is an OCaml mode for GNU Emacs.  It handles automatic indentation
of Objective Caml and Caml Light code.  Key parts of the code are
highlighted using Font-Lock.  Support to run an interactive Caml
toplevel and debbuger is provided.

Install this package if you need to edit OCaml code in Emacs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%build
%make_build

%install
# The upstream 'make install' rule invokes opam to find install directories.
# Install directly to avoid a dependency on opam.
mkdir -p $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}
echo %{version} > $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}/version
install -m 0644 *.el *.elc $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}
mkdir -p $RPM_BUILD_ROOT/%{emacs_startdir}
mv $RPM_BUILD_ROOT/%{emacs_lispdir}/%{pkg}/tuareg-site-file.el \
   $RPM_BUILD_ROOT/%{emacs_startdir}

%check
make check

%files
%doc CHANGES.md README.md
%license COPYING

%files -n emacs-%{pkg}
%license COPYING
%{emacs_lispdir}/%{pkg}/*.elc
%{emacs_lispdir}/%{pkg}/*.el
%{emacs_lispdir}/%{pkg}/version
%{emacs_startdir}/*.el
%dir %{emacs_lispdir}/%{pkg}

%changelog
%autochangelog
