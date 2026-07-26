%global source0_hash e67c5726fc1fe53574c2e8b5f72634f1359d0f53586a555eb2489fafd7c81640

# Use QORTEC's fork for now since upstream appears unmaintained.
# See https://github.com/pdewacht/brlaser/issues/145
%global forgeurl https://github.com/Owl-Maintain/brlaser

Name:           printer-driver-brlaser
Version:        6.2.7
%forgemeta
Release:        %autorelease
Summary:        Brother laser printer driver

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cups-devel
Requires:       cups-filesystem
Requires:       ghostscript

%description
brlaser is a CUPS driver for Brother laser printers.

Although most Brother printers support a standard printer language
such as PCL or PostScript, not all do. If you have a monochrome
Brother laser printer (or multi-function device) and the other open
source drivers don't work, this one might help.

For a detailed list of supported printers, please refer to
%{forgeurl}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_cups_serverbin}/filter/rastertobrlaser
%{_datadir}/cups/drv/brlaser.drv
%doc README.md
%license COPYING

%changelog
%autochangelog
