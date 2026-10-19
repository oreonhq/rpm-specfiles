%global source0_hash ce648d6531c3d55501078073e08a18d70e880b6329b5b168a59db5213d048491
%ifarch i686
%global _lto_cflags %nil
%endif
Summary:        A powerful visualization and data analysis tool
Name:          extrema
Version:       4.4.5
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           http://exsitewebware.com/extrema/
Source0:        http://downloads.sourceforge.net/extrema/extrema-%{version}.tar.gz
Patch:         extrema-4.2.10.desktop.patch
Patch:         extrema-4.4.5-gcc46.patch
Patch:         extrema-4.4.5-wx3.0.patch
Patch:         extrema-4.4.5-wx3.0-2.patch
Patch:         extrema-4.4.5-wx3.2.patch
Patch:         extrema-4.4.5-gcc16.patch
Requires:      extrema-help
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
Extrema is a powerful visualization and data analysis tool that
enables researchers to quickly distill their large, complex data sets
into meaningful information. Its flexibility, sophistication, and
power allow you to easily develop your own commands and create highly
customized graphs.

%package       help
Summary:       Help files for Extrema
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
%description   help
This package contains help files for Extrema.

%package       doc
Summary:       Extrema documentation in PDF format
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
%description   doc
This package contains Getting Started, User Guide and other
documentation in PDF format for Extrema.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static CXXFLAGS="%{optflags} -DNDEBUG"
%make_build
convert Images/%{name}.gif %{name}.png
%install
%make_install
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -m 0644 -D %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -f %{buildroot}%{_libdir}/lib%{name}.{la,a}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n extrema-help -f %{oreon_filedir}/extrema-help.list
%files -n extrema-doc -f %{oreon_filedir}/extrema-doc.list

%changelog

%autochangelog
