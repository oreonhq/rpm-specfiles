%global source0_hash c585a2f4a10b397e460a95043d59ac79cf4442fbb45a6e14a1e27ef9febaed73

%define         machines %{_datadir}/openmsx/machines

Name:           cbios
Version:        0.29a
Release:        18%{?dist}
Summary:        A third party BIOS compatible with the MSX BIOS
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://cbios.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.zip
BuildArch:      noarch
BuildRequires:  sjasm
BuildRequires: make

%description
C-BIOS is a BIOS compatible with the MSX BIOS written from scratch by BouKiCHi.
It is available for free, including its source code and can be shipped with MSX
emulators so they are usable out-of-the-box without copyright issues.

# Build c-bios support for different msx emulators as sub packages, cbios has
# support for blueMSX, NLMSX, openMSX, RuMSX but at the moment we only support
# openmsx (others not available for Linux yet).
%package openmsx
Summary:        C-BIOS support for openMSX
Requires:       cbios = %{version}-%{release}
Requires:       openmsx >= 0.9.2

%description openmsx
Adds C-BIOS support for openMSX, a third party MSX compatible BIOS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's/\r//' doc/*.txt
# Character encoding fixes
iconv -f iso8859-1 doc/cbios.txt -t utf8 > doc/cbios.conv \
    && /bin/mv -f doc/cbios.conv doc/cbios.txt

%build
make %{?_smp_mflags} Z80_ASSEMBLER=sjasm

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{machines}
install -pm 0644 derived/bin/* %{buildroot}%{_datadir}/%{name}

# Install openmsx configuration and symlinks to cbios
cp -a configs/openMSX/C-BIOS_MSX* %{buildroot}%{machines}
for i in %{buildroot}%{_datadir}/%{name}/*.rom; do
    ln -s --target-directory=%{buildroot}%{machines} \
        ../../%{name}/$(basename $i)
done

%files
%{_datadir}/%{name}
%doc doc/cbios.txt doc/chkram.txt

# We don't own the parent directories here, because they are owned by openmsx,
# also we don't set hardwareconfig.xml as %%config because they are not
# intended to be changed by the end user.
%files openmsx
%{machines}/*
%doc configs/openMSX/README.txt

%changelog
%autochangelog
