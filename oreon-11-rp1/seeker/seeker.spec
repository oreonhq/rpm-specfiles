%global source0_hash 5d638cbd716e35fb267d50708fc706630158aade61f22ad3ed16c49c493b34c5
Name:           seeker
Version:        3.0
Release:        1%{?dist}
Summary:        Random access disk benchmark utility
License:        GPL-2.0-only and CC-BY-SA-4.0
URL:            http://www.linuxinsight.com/how_fast_is_your_disk.html
Source0:        http://smp.if.uj.edu.pl/~baryluk/seeker_baryluk.c
Source1:        %{name}.LICENSE
Source2:        %{name}-docs.tar.gz
Patch0:         %{name}-3.0-timeout-blockalign-623667.patch
# oreon:deps
BuildRequires:  gcc
# /oreon:deps
%description
Seeker is a simple utility that reads small pieces of data from a raw
disk device in a random access pattern, and reports the average number
of seeks per second, and calculated random access time of the disk.
The seeker variant included in this package is the multithreaded one
by Witold Baryluk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -a 2
install -pm 644 %{SOURCE0} $(basename %{SOURCE0}) # for debuginfo, Patch0
%patch -P0
cp -p %{SOURCE1} LICENSE

%build

%{__cc} -D_GNU_SOURCE $RPM_OPT_FLAGS -std=gnu17 $RPM_LD_FLAGS -pthread \
    $(basename %{SOURCE0}) -o seeker
%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 seeker $RPM_BUILD_ROOT%{_sbindir}/seeker
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
