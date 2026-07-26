%global source0_hash 06c8870f88b5919862910dec354576dbcfecee7e6b7202b92a730ea0903c01db

%global commit0 c40fb2289952f4f120cc10a5a4c82a6fb88442dc

# The upstream makefile gets version information by invoking git. We can't
# do that. We can still use what the Makefile calls GIT_REV, because that's
# our shortcommit0 variable extracted from commit0 below.  We have to
# hard-code VER and VER_HASH here, as ver0 and verhash0.  When updating this
# package spec for a new git snapshot, clone the git repo, run make in it,
# and inspect the generated version_(has).cc to determine the correct values.
%global ver0 0.1+328+0
%global verhash0 34321

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           arachne-pnr
Version:        0.1
Release:        0.27.20190729git%{shortcommit0}%{?dist}
Summary:        Place and route for FPGA compilation
License:        MIT
URL:            https://github.com/cseed/arachne-pnr
Source0:        https://github.com/cseed/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# https://github.com/YosysHQ/arachne-pnr/issues/126
Patch0:         use-std-priority-queue.patch
Patch1:         make-use-of-emplace.patch

# patch the tests, which give equivalent but different results
# (the meaning of the verilog didn't change, but the order and variable numbers did)
Patch2:         test-fixup.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Continue building on s390x, but skip the tests
# those need yosys and it doesn't build on s390x
# TODO: subset tests to run on s390x without yosys
%ifnarch s390x
%bcond check 1
%else
%bcond check 0
%endif

BuildRequires:  gcc-c++
BuildRequires:  icestorm
BuildRequires:  make
%if %{with check}
# shasum,yosys needed to complete simpletests
BuildRequires:  perl(Digest::SHA)
BuildRequires:  yosys
%endif

%description
Arachne-pnr implements the place and route step of the hardware
compilation process for FPGAs. It accepts as input a technology-mapped
netlist in BLIF format, as output by the Yosys synthesis suite for
example. It currently targets the Lattice Semiconductor iCE40 family
of FPGAs. Its output is a textual bitstream representation for
assembly by the IceStorm icepack command. The output of icepack is a
binary bitstream which can be uploaded to a hardware device.

Together, Yosys, arachne-pnr and IceStorm provide an fully open-source
Verilog-to-bistream tool chain for iCE40 1K and 8K FPGA development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit0} -p1

# can't use git from Makefile to extract version information
sed -i 's/^VER =.*/VER = %{ver0}/' Makefile
sed -i 's/^GIT_REV =.*/GIT_REV = %{shortcommit0}/' Makefile
sed -i 's/^VER_HASH =.*/VER_HASH = %{verhash0}/' Makefile

%build
make %{?_smp_mflags} \
     CXXFLAGS="%{optflags}" \
     PREFIX="%{_prefix}" \
     ICEBOX="%{_datadir}/icestorm"

%install
make install PREFIX="%{_prefix}" \
             DESTDIR="%{buildroot}" \
             ICEBOX="%{_datadir}/icestorm"

%check
%if %{with check}
make simpletest %{?_smp_mflags} \
     CXXFLAGS="%{optflags} -Isrc/" \
     PREFIX="%{_prefix}" \
     ICEBOX="%{_datadir}/icestorm"
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}

%changelog
%autochangelog
