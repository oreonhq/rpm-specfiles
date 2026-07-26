%global source0_hash 7645e5bf3e21671f42c0c4dce8fa57a9d446d72573297f1a3526aef49a68baf2

%global debug_package %{nil}
%global commit 8e1c0a5699c34bc4952e86dc0509070770f2c625

Name:           mum-hash
Version:        0
Release:        12.20210318git%{commit}%{?dist}
Summary:        Fast non-cryptographic hash function

License:        MIT
URL:            https://github.com/vnmakarov/mum-hash
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

%define common_desc MUM hash is a fast non-cryptographic hash function suitable for \
different hash table implementations.

%description
%{common_desc}

%package  devel
Summary:  %{summary}
Provides: mum-hash-static = %{version}-%{release}

%description devel
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 mum.h %{buildroot}%{_includedir}
install -p -m 644 mum-prng.h %{buildroot}%{_includedir}
install -p -m 644 mum512.h %{buildroot}%{_includedir}

%files devel
%doc README.md ChangeLog
%{_includedir}/mum*h

%changelog
%autochangelog
