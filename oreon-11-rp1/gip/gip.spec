%global source0_hash c525886d90d496839b6a51e3ab771f2511abfea2fcb78cfcfe82059a4e53c6b9

%undefine _ld_as_needed

Name:       gip
Version:    1.7.0
Release:    20%{?dist}
Summary:    Internet Protocol Calculator for Gnome

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later

Url:        http://code.google.com/p/gip/
Source0:    https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/gip/%{name}-%{version}-1.tar.gz
Patch1:     %{name}-%{version}-ubuntu.patch
Patch2:     %{name}-%{version}-c++11.patch

BuildRequires:  gtkmm24-devel
BuildRequires:  intltool
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Gip is an application for making IP address based calculations.
For example, it can display IP addresses in binary format.
It is also possible to calculate subnets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}-1

sed -i 's|CFLAGS="-std=c++11|CFLAGS="$(echo $CFLAGS) -std=c++11|' build.sh
sed -i 's|LFLAGS=`pkg-config $REQUIRED_LIBS --libs`|LFLAGS="$(echo $LDFLAGS) `pkg-config $REQUIRED_LIBS --libs`"|' build.sh
sed -i "s|INST_LIBDIR=\"\$INST_PREFIX/lib/\$EXECUTABLE\"|INST_LIBDIR=\"\$INST_PREFIX/share/\$EXECUTABLE\"|" build.sh
sed -i "s|INST_PIXMAPDIR=\"\$INST_PREFIX/lib/\$EXECUTABLE\"|INST_PIXMAPDIR=\"\$INST_PREFIX/share/\$EXECUTABLE\"|" build.sh

%build
%set_build_flags
./build.sh --prefix %{_prefix}

%install
mkdir -p %{buildroot}%{_prefix}
./build.sh --install --prefix %{buildroot}%{_prefix}
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/calc.png
%{_datadir}/mime/packages/%{name}.xml

%changelog
%autochangelog
