%global source0_hash 646f12ad4552aa20ed5a8e82fb6fd1d0ccd6e0c64d2bc00e7aa36de1942ba0aa

%global git_commit 340003eb0846b069c3edef19ed3363b8ac7b5215
%global git_date 20230403
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:             kalibrate-rtl
URL:              http://github.com/steve-m/kalibrate-rtl
Version:          0.4.1^%{git_suffix}
Release:          10%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
BuildRequires:    gcc-c++
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    rtl-sdr-devel
BuildRequires:    fftw-devel
BuildRequires:    libusbx-devel
BuildRequires:    make
Summary:          GSM based frequency calibration for rtl-sdr
Source0:          https://github.com/steve-m/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

%description
Kalibrate, or kal, can scan for GSM base stations in a given frequency band and
can use those GSM base stations to calculate the local oscillator frequency
offset.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}
autoreconf -fi

%build
%configure
%make_build

%install
%make_install

# Rename kal to kal-rtl to avoid possible conflicts
mv %{buildroot}%{_bindir}/kal %{buildroot}%{_bindir}/kal-rtl

%files
%license COPYING
%doc README.md AUTHORS
%{_bindir}/*

%changelog
%autochangelog
