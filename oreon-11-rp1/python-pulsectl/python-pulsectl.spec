%global source0_hash 288d6715232ac6f3dcdb123fbecaa2c0b9a50ea4087e6e87c3f841ab0a8a07fc
%global pypi_name pulsectl
Name:           python-%{pypi_name}
Version:        24.12.0
Release:        1%{?dist}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio
License:        MIT
URL:            https://pypi.org/project/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/%/%{pypi_name/%{pypi_name-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pulseaudio-libs
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Python (3.x and 2.x) high-level interface and ctypes-based bindings
for PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).

%package     -n python3-%{pypi_name}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio
%description -n python3-%{pypi_name}
Python 3.x high-level interface and ctypes-based bindings for
PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{pypi_name}-%{version}

%build

%{py3_build}
%install
%{py3_install}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pulsectl -f %{oreon_filedir}/python3-pulsectl.list

%changelog

%autochangelog
