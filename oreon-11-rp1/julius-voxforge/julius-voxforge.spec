%global source0_hash 143d1e1290d9c6016a8a12151d4ffdd4b96e4c13ea73c153814b5b094d4db0d0

%global year  2013
%global month 03
%global day   01

Name:		julius-voxforge
Version:	%{year}.%{month}.%{day}
Release:	26%{?dist}
Summary:	VoxForge Acoustic Model files for Julius
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.voxforge.org/
Source0:	http://www.repository.voxforge1.org/downloads/Nightly_Builds/current/Julius-4.2-Quickstart-Linux_AcousticModel-%{year}-%{month}-%{day}.tgz
BuildArch:	noarch
Requires:	julius

%description
VoxForge was set up to collect transcribed speech for use with Free and
Open Source Speech Recognition Engines (on Linux, Windows and Mac).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
sed -i 's/\r//' LICENSE

%build

%install
install -d %{buildroot}%{_datadir}/%{name}/acoustic
install -m644 acoustic_model_files/hmmdefs acoustic_model_files/macros acoustic_model_files/tiedlist %{buildroot}%{_datadir}/%{name}/acoustic

%files
%doc LICENSE README Sample.jconf
%{_datadir}/%{name}/acoustic

%changelog
%autochangelog
