%global source0_hash 1be43b48a4cc704ef84b5673b4fc78323709fd0d61c18dbd364ac89a38e2ab31

Name:           R-AsioHeaders
Version:        %R_rpm_version 1.30.2-1
Release:        %autorelease
Summary:        Asio C++ Header Files

License:        BSL-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel < 1.30.2-1

Provides:       bundled(asio) = 1.30.2
Requires:       openssl-devel
Requires:       openssl-devel-engine
Recommends:     boost-devel

%description
'Asio' is a cross-platform C++ library for network and low-level I/O
programming that provides developers with a consistent asynchronous model using
a modern C++ approach. It is also included in Boost but requires linking when
used with Boost. Standalone it can be used header-only (provided a recent
compiler). 'Asio' is written and maintained by Christopher M. Kohlhoff, and
released under the 'Boost Software License', Version 1.0.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
