%global source0_hash c208baf759134da27012042ccc30df7d995ed038d7d5602db7dbda3becb34827

# RPM Spec file for retry

Name:      retry
Version:   1.0.6
Release:   2%{?dist}
Summary:   Repeat a command until success
License:   Apache-2.0

URL:       https://github.com/minfrin/%{name}
Source0:   %{URL}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires: clang
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
The tool repeats the given command until the command is successful,
backing off with a configurable delay between each attempt.

Retry captures stdin into memory as the data is passed to the repeated
command, and this captured stdin is then replayed should the command
be repeated. This makes it possible to embed the retry tool into shell
pipelines.

Retry captures stdout into memory, and if the command was successful
stdout is passed on to stdout as normal, while if the command was
repeated stdout is passed to stderr instead. This ensures that output
is passed to stdout once and once only.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/retry
%{_mandir}/man1/retry.1*

%doc AUTHORS ChangeLog README
%license COPYING

%changelog
%autochangelog
