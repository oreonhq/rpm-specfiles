%global source0_hash none

Name:           gstreamer1-vaapi
Version:        1.28.7
Release:        %autorelease
Summary:        GStreamer VA API plugins (provided by plugins-bad)
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gstreamer.freedesktop.org/
BuildArch:      noarch

Requires:       gstreamer1-plugins-bad-free >= %{version}
Provides:       gstreamer1-vaapi = %{version}-%{release}
Obsoletes:      gstreamer1-vaapi < %{version}-%{release}

%description
VA API decode/encode/display plugins now ship in gstreamer1-plugins-bad-free.
This package pulls that in.

%package devel
Summary:        Devel bits for GStreamer VA API
Requires:       gstreamer1-plugins-bad-free-devel >= %{version}
Requires:       %{name} = %{version}-%{release}
Provides:       gstreamer1-vaapi-devel = %{version}-%{release}
Obsoletes:      gstreamer1-vaapi-devel < %{version}-%{release}

%description devel
Headers and pkg-config for VA plugins now come from gstreamer1-plugins-bad-free-devel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%build

%install

%files

%files devel

%changelog
%autochangelog
