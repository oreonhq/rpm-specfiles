%global source0_hash 8e8532111d0163628eb828a60d67b53133afad3f710b1967e69d3b8eee28a811

%global     detectorver 1.1

Name:           unar
Version:        1.10.8
Release:        15%{?dist}
Summary:        Multi-format extractor
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://theunarchiver.com/command-line
Source0:        https://github.com/MacPaw/XADMaster/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/MacPaw/universal-detector/archive/%{detectorver}/universal-detector-%{detectorver}.tar.gz
Patch1: unar-int-conversion.patch
BuildRequires:  bzip2-devel
BuildRequires:  gcc-objc
BuildRequires:  gcc-c++
BuildRequires:  gnustep-base-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(wavpack)

%description
The command-line utilities lsar and unar are capable of listing and extracting
files respectively in several formats including RARv5, RAR support includes
encryption and multiple volumes, unar can serve as a free and open source
replacement of unrar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
tar -xf %{SOURCE1}
%patch -P1 -p1
mv universal-detector-%{detectorver} UniversalDetector
rm -fr __MACOSX The\ Unarchiver
# recursively remove executable bit from every file, skipping directories
find . -type f -print0 | xargs -0 chmod -x

%build
# LTO is able to more thoroughly propagate constants and as a result
# exposes the constant 0 to a point where an Objective-C object with
# a catchable type must be used.  Disable LTO until the package
# gets fixed
%define _lto_cflags %{nil}
export OBJCFLAGS="%{optflags}"
#export OBJCFLAGS=`gnustep-config --objc-flags`
make -C XADMaster-%{version} -f Makefile.linux \
%if 0%{?rhel} >= 8
  OBJCC=gobjc
%endif

%install
pushd XADMaster-%{version}
install -d %{buildroot}%{_bindir}
install -pm755 unar lsar %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -pm644 Extra/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 Extra/lsar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/lsar
install -pm644 Extra/unar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/unar
popd

%files
%license XADMaster-%{version}/LICENSE
%{_bindir}/lsar
%{_bindir}/unar
%{_mandir}/man1/*.1*
%{_datadir}/bash-completion/completions/*

%changelog
%autochangelog
