Name:		    secvarctl
Version:	    1.1.0
Release:	    %autorelease
Summary:	    Suite of tools to manipulate and generate Secure Boot variables on POWER
License:	    Apache-2.0
URL:		    https://github.com/open-power/secvarctl
Source0:        https://github.com/open-power/secvarctl/archive/v1.1.0/secvarctl-1.1.0.tar.gz
Source1:        https://github.com/ibm/libstb-secvar/archive/ce98be9d15ac2df062726b4451f0ec0c0b27fbf2.tar.gz
# oreon url source checksums begin
%global source0_sha256 19f5925c9f032c92c9f1eb919816945b36412a2c78841bdf1f25c83f9c1e890b
%global source0_file secvarctl-1.1.0.tar.gz
%global source1_sha256 b1adf3dd540ad62ec9e5eb36d1f8ccb219c22b755f7b1c9bdd6a3980393a6af2
%global source1_file ce98be9d15ac2df062726b4451f0ec0c0b27fbf2.tar.gz
# oreon url source checksums end

BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	openssl-devel
BuildRequires:  libasan

Provides:       bundled(libstb-secvar)

%description
Suite of tools to manipulate and generate Secure Boot variables on POWER.

The purpose of this tool is to simplify and automate the process of reading and
writing secure boot keys. secvarctl allows the user to communicate, via terminal
commands, with the keys efficiently. It is supporting automate process of the
both host and guest secure boot keys.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/secvarctl-1.1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "19f5925c9f032c92c9f1eb919816945b36412a2c78841bdf1f25c83f9c1e890b" || { echo "oreon: Source0 SHA256 mismatch for secvarctl-1.1.0.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/ce98be9d15ac2df062726b4451f0ec0c0b27fbf2.tar.gz; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b1adf3dd540ad62ec9e5eb36d1f8ccb219c22b755f7b1c9bdd6a3980393a6af2" || { echo "oreon: Source1 SHA256 mismatch for ce98be9d15ac2df062726b4451f0ec0c0b27fbf2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
tar xf %{SOURCE1} -C external/libstb-secvar --strip-components=1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check
%ifarch ppc64le
make check
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-1
- Import
