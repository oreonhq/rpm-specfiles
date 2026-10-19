%global source0_hash fd8d5804c27efb22d63579aba5ab69d70ad115f5eb8c7bd1d63d5024113f067b
Name:           pavumeter
Version:        0.9.3
Release:        1%{?dist}
Summary:        Volume meter for PulseAudio
License:        GPL-2.0-or-later
URL:            http://0pointer.de/lennart/projects/pavumeter
Source0:        http://0pointer.de/lennart/projects/pavumeter/pavumeter-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtkmm24-devel
BuildRequires:  lynx
BuildRequires:  make
BuildRequires:  pkgconfig(libpulse)
# /oreon:deps
%description
PulseAudio Volume Meter (pavumeter) is a simple GTK volume meter for the
PulseAudio sound server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    --add-category="X-Fedora" --vendor="" \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
