%global source0_hash 9228650edc48ad5deeab5d92272e242e906f90d292c90af132a3f20d9354735a
%global majorversion 7.2
Name:           ipe
Version:        7.2.30
Release:        1%{?dist}
Summary:        Drawing editor for creating figures in PDF or PostScript formats
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            http://ipe.otfried.org/
Source0:        https://github.com/otfried/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         %{name}-%{version}-gcc11.patch
Requires:       tex(latex)
Requires:       urw-fonts
Requires:       xdg-utils
Requires:       qt5-qtsvg
Provides:       ipe(api) = %{version}
Provides:       ipetoipe = %{version}
Provides:       ipetopng = %{version}
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libspiro-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qtspell-qt6-devel
# /oreon:deps
%description
Ipe is a drawing editor for creating figures in PDF or (encapsulated)
Postscript format. It supports making small figures for inclusion into
LaTeX-documents as well as making multi-page PDF presentations that
can be shown on-line with a PDF viewer

%package devel
Summary: Development files and documentation for designing Ipelets
Requires: %{name} = %{version}-%{release}
Requires: qt5-qtbase-devel
%description devel 
This packages contains the files necessary to develop Ipelets, which are
plugins for the Ipe editor.

%package doc
BuildArch: noarch
Summary: Documentation of Ipe
Requires: %{name} = %{version}-%{release}
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{name}-%{version} -q
%patch 0 -p1

# fix files permissions
find src -type f -exec chmod -x {} +

%build

export QTDIR=%{qtdir}
pushd src
%make_build LUA_CFLAGS="`pkg-config --cflags lua`" \
     LUA_LIBS="`pkg-config --libs lua`" \
     MOC=/usr/lib64/qt6/libexec/moc \
     IPEPREFIX="%{_prefix}" IPELIBDIR="%{_libdir}" \
     IPELETDIR="%{_libdir}/%{name}/%{version}/ipelets" \
     IPECURL=1 IPEGSL=1
popd 
%install
pushd src
make INSTALL_ROOT=%{buildroot} install \
     IPEPREFIX="%{_prefix}" IPELIBDIR="%{_libdir}" \
     IPELETDIR="%{_libdir}/%{name}/%{version}/ipelets" \
     INSTALL_PROGRAMS="install -m 0755"
popd
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ipe-devel -f %{oreon_filedir}/ipe-devel.list
%files -n ipe-doc -f %{oreon_filedir}/ipe-doc.list

%changelog

%autochangelog
