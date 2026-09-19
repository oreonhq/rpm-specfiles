%global source0_hash 44325c646aa565c4d11faf8f97cf86ae407f56413ab4f898cf8d8c2688e88e40

Name:           gimp-wavelet-denoise-plugin
Version:        0.4
Release:        2%{?dist}
Summary:        Gimp wavelet denoise plugin

License:        GPL-2.0-or-later
URL:            https://github.com/mrossini-ethz/gimp-wavelet-denoise
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch0:         gimp-wavelet-denoise-plugin-fno-common-fix.patch

BuildRequires:  gcc
BuildRequires:  gimp-devel >= 2.4.0
BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  make

Requires:       gimp >= 2.4

%description
The wavelet denoise plugin is a tool to reduce noise in each channel of an
image separately. The default colour space to do denoising is YCbCr which
has the advantage that chroma noise can be reduced without affecting image
details. Denoising in CIELAB (L*a*b*) or RGB is available as an option.
The user interface allows colour mode and preview channel selection.
The denoising threshold can be set for each colour channel independently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gimp-wavelet-denoise-%{version}
sed -i -e 's/CFLAGS.*/& $(shell echo $$CFLAGS)/' src/Makefile
sed -i -e "s!    59 Temple Place, Suite 330, Boston, MA  02111-1307  USA!51\ Franklin Street,\ Fifth\ Floor,\ Boston,\ MA!" COPYING

%build
%set_build_flags
%make_build

%install
GIMP_PLUGINS_DIR=`gimptool-2.0 --gimpplugindir`
sed -i "s|/usr/share/locale|%{buildroot}%{_datadir}/locale|" po/Makefile
mkdir -p %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
install -m 0755 -p src/wavelet-denoise %{buildroot}$GIMP_PLUGINS_DIR/plug-ins
mkdir -p %{buildroot}%{_datadir}/locale/de/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/it/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/et/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES
make install po
%find_lang gimp20-wavelet-denoise-plug-in

%files -f gimp20-wavelet-denoise-plug-in.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/gimp/2.0/plug-ins/wavelet-denoise

%changelog
%autochangelog
