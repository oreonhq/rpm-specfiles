%global source0_hash 74d8f656864787c4b6819cdfdb38d9f52793ea3197f9ac6741f9c7dbb7ce2124

%global with_tag       0

Name:                  rtl-wmbus
%global forgeurl       https://github.com/xaelsouth/%{name}
%global the_binary     rtl_wmbus

%if %{with_tag}
%global tag            0.0.0
Version:               %{tag}
%else
%global date           20240118
%global commit         20cafdcecf28121cb4d5546cfe9cbc1822a70a03
Version:               0
%endif

%forgemeta

Release:               24%{?dist}
Summary:               Software defined receiver for wireless M-Bus with RTL-SDR
# Automatically converted from old format: BSD - review is highly recommended.
License:               LicenseRef-Callaway-BSD
Url:                   %{forgeurl}
Source0:               %{forgesource}

BuildRequires:         make
BuildRequires:         /usr/bin/git
BuildRequires:         gcc
BuildRequires:         fixedptc-devel

Requires:              /usr/bin/rtl_sdr

%description
rtl-wmbus is a software defined receiver for Wireless-M-Bus.
It is written in plain C and uses RTL-SDR to interface with RTL2832-based
hardware.

Wireless-M-Bus is the wireless version of M-Bus
("Meter-Bus", http://www.m-bus.com), which is an European standard for
remote reading of smart meters.

The primary purpose of rtl-wmbus is experimenting with digital signal
processing and software radio.

rtl-wmbus can be used on resource constrained devices such as Raspberry Pi Zero
or Raspberry PI B+ overclocked to 1GHz. Any Android based tablet will do
the same too.

rtl-wmbus provides:
  - filtering
  - FSK demodulating
  - clock recovering
  - mode T1 and mode C1 packet decoding

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -S git
# Remove bundled fixedptc library and build directory
rm -rf include build

# Split the LICENSE from the README.md
awk '/^  License/ {dump=1; next} \
     /^  -------/ {next} \
     /.*/         {if (dump) {print}}' \
     README.md >LICENSE

%build
%set_build_flags
export LIB="%{__global_ldflags} -lm"
%{make_build} \
    COMMIT_HASH="" \
    TAG=%{version}%{?distprefix} \
    BRANCH="" \
    CHANGES="" \
    TAG_COMMIT_HASH=""

%install
install -p -m 0755 -D build/%{the_binary} %{buildroot}%{_bindir}/%{the_binary}

%files
# The license is in the documentation file
%license LICENSE
%doc README.md
%{_bindir}/%{the_binary}

%changelog
%autochangelog
