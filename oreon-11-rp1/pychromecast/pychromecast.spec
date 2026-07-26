%global source0_hash 75571ef1bdb9808a52227ba47ae46281332bbe67eaebc26aee947cdc1e3e5a67

Name:           pychromecast
Version:        13.1.0
Release:        11%{?dist}
Summary:        Python library to communicate with the Google Chromecast

License:        MIT
URL:            https://github.com/home-assistant-libs/pychromecast
Source0:        https://github.com/home-assistant-libs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# runtime requires to at least perform an import test in %%check
BuildRequires:  python3-casttube
BuildRequires:  python3-protobuf
BuildRequires:  python3-zeroconf

%description
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%package -n python3-chromecast
Summary:  Library for Python 3 to communicate with the Google Chromecast
%{?python_provide:%python_provide python3-chromecast}

%description -n python3-chromecast
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pychromecast

%check
%py3_check_import pychromecast

%files -n python3-chromecast -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
