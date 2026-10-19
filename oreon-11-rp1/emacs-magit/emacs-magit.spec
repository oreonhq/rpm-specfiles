%global source0_hash cf2b437f2ad3b2aa2cc2379e7d7bb6c9a8ba6f246b03505ebac6a0f8417afb51
%define pkg magit
%define pkgname Magit
Name:           emacs-%{pkg}
Version:        4.7.1
Release:        1%{?dist}
Summary:        Emacs interface to the most common Git operations
License:        GPL-3.0-or-later
URL:            https://magit.vc
Source0:        https://github.com/magit/magit/archive/refs/tags/v%{version}.tar.gz
Source1:        magit-init.el
BuildArch:      noarch
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-async emacs-dash emacs-transient emacs-with-editor
Requires:       git-core
Obsoletes:      emacs-%{pkg}-el < %{version}-%{release}
Provides:       emacs-%{pkg}-el = %{version}-%{release}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-async
BuildRequires:  emacs-dash
BuildRequires:  emacs-transient
BuildRequires:  emacs-with-editor
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
%{pkgname} is an add-on package for GNU Emacs. It is an interface to
the Git source-code management system that aims to make the most
common operations convenient.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkg}-%{version}

%global MAKE_PARMS VERSION="%{version}-%{release}" LOAD_PATH="-L %{_emacs_sitelispdir}/dash -L %{_emacs_sitelispdir}/transient -L %{_emacs_sitelispdir}/with-editor -L $(pwd)/lisp"

%build

make BUILD_MAGIT_LIBGIT=false \
    %{MAKE_PARMS} \
    versionlib lisp info
%check

emacs --batch -L lisp -l %{pkg} -f %{pkg}-version 2>&1 \
    | grep "%{pkgname} %{version}"
%install
make install-lisp install-info \
    %{MAKE_PARMS} \
    DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} BUILD_MAGIT_LIBGIT=false
mkdir -p %{buildroot}%{_emacs_sitestartdir}/
cp -p %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
