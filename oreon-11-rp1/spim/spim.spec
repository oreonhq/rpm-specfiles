%global source0_hash f163fc3e9d58ea9d63d24c0df2b0ff374354d5ecfeda8d8aefab8e6e6ffa9924
Name:           spim
Version:        20230804
Release:        1%{?dist}
Summary:        An assembly language MIPS32 simulator
License:        BSD-3-Clause
URL:            http://spimsimulator.sourceforge.net/
Source0:        spimsimulator-spim-20230804.tar.gz
Source1:        spimsimulator-CPU-20230804.tar.gz
Source2:        spimsimulator-Documentation-20230804.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
spim is a self-contained simulator that runs MIPS32 programs. It reads and
executes assembly language programs written for this processor. spim also
provides a simple debugger and minimal set of operating system services.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -T -a 0 -c
%setup -q -T -D -a 1 -c
%setup -q -T -D -a 2 -c -n spim-%{version}/spim

# Fix EOL encoding.
sed 's/\r//' README > README.unix
touch -r README README.unix
mv -f README.unix README

# Fix some permissions.
find . -type f -perm /0111 -print0 | xargs -0 chmod a-x

%build

CFLAGS="%{optflags}" make %{?_smp_mflags}
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 -D Documentation/spim.man %{buildroot}%{_mandir}/man1/spim.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
