%global source0_hash c1769fea45c23bf892bdbf524c92ddf83eae21b1ddba358d4173155aadea898e
Name:           gummi
Version:        0.8.3
Release:        1%{?dist}
Summary:        A simple LaTeX editor
License:        MIT
URL:            https://github.com/alexandervdm/gummi
Source0:        https://github.com/alexandervdm/gummi/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires:       texlive-latex
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  gtkspell3-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  poppler-glib-devel
BuildRequires:  tex-synctex
BuildRequires:  texlive-lib-devel
# /oreon:deps
%description
Gummi is a LaTeX editor written in the C programming language using the
GTK+ interface toolkit. It was designed with simplicity and the novice
user in mind, but also offers features that speak to the more advanced user.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="$CFLAGS -std=gnu17"
%configure
%make_build
%install
%make_install
%find_lang %{name}
desktop-file-install                                 \
    --remove-key="Version"                           \
    --add-category="Publishing;"                     \
    --dir=%{buildroot}%{_datadir}/applications       \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
