%global source0_hash bae11f5703c0bbe35437f39348bb388d719413bc3135ffc3d1b06bb9bbcf5963

%global commit f4d2682804931e7aea02a869137344bb5452a3cd
%global build_date 20151118

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global posttag %{build_date}git%{shortcommit}

Name:		cpulimit
Summary:	CPU Usage Limiter for Linux

# The main program sources are GPLv2+.
# There is one file, "src/memrchr.c", under the MIT license;
# however, that is used only for macOS builds.
License:	GPL-2.0-or-later

Epoch:		1
Version:	0.2^%{posttag}
Release:	4%{?dist}

URL:		https://github.com/opsengine/cpulimit
Source0:	https://github.com/opsengine/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch0:		0000-fix-includes.patch
Patch1:		0001-incompatible-pointer-type.patch

BuildRequires:  gcc
BuildRequires:  make

%description
cpulimit is a simple program which attempts to limit the CPU usage of a process
(expressed in percentage, not in CPU time). This is useful to control batch
jobs, when you don't want them to eat too much CPU. It does not act on the nice
value or other scheduling priority stuff, but on the real CPU usage. Also, it
is able to adapt itself to the overall system load, dynamically and quickly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%build
%make_build

%install
install -Dp -m 755 src/cpulimit %{buildroot}/%{_bindir}/cpulimit

%files
%{_bindir}/cpulimit
%doc README.md
%license LICENSE

%changelog
%autochangelog
