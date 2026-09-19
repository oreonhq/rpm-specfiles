%global source0_hash 5cc04732ef32850d5878b28fbd8b85798d979a025990654aceeaa379bcc9596d

Name:		mp3gain
Version:	1.6.2

%global tarball_version %(echo %version|sed 's/\\./_/g')

Release:	17%{?dist}
Summary:	Lossless MP3 volume adjustment tool

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://mp3gain.sourceforge.net/
Source0:	https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{tarball_version}-src.zip
# copied from Debian
Source1:	%{name}.1
Source2:	README.method
Patch2:		%{name}-cflags-1.5.2.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: mpg123-devel

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same
volume. It does not just do peak normalization, as many normalizers
do. Instead, it does some statistical analysis to determine how loud
the file actually sounds to the human ear. Also, the changes MP3Gain
makes are completely lossless. There is no quality lost in the change
because the program adjusts the mp3 file directly, without decoding
and re-encoding.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{tarball_version}
%patch -P2 -p0 -b .cflags
install -p -m 644 %{SOURCE2} .
sed -i 's/\r//' lgpl.txt

%build
%make_build

%install
install -Dp -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc README.method
%license lgpl.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
