%global source0_hash 6eb8c3ba7162a9952edd36195c17e4444003ea42a69394d788b0bd76291bc88e

Name:           unifying-receiver-udev
Version:        0.2
Release:        27%{?dist}
Summary:        udev rules for user access to Logitech Unifying Receiver
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://www.brouhaha.com/~eric/software/%{name}/
Source0:        http://www.brouhaha.com/~eric/software/%{name}/download/%{name}-%{version}.tar.gz
BuildArch:      noarch

# Adds device 046d/c52f to the udev rules, fixing bug 1202977. Rather than
# trying to submit this change upstream, a better solution is probably to use
# the udev rules shipped with solaar itself. See the bug for more details.
Patch0:         unifying-receiver-udev-046d-c52f.patch

%global udev_order 69

%global udev_rules_dir /usr/lib/udev/rules.d
# Do not use %%{_libdir}, because udev rules always go into
# /usr/lib/udev/rules.d, and not (on x86_64) /usr/lib64/udev/rules.d

%description
Udev rules to allow user access to the Logitech Unifying Receiver, e.g., for
use with ltunify, pairing_tool, or Solaar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

%install
install -D -p -m 644 unifying-receiver.rules %{buildroot}%{udev_rules_dir}/%{udev_order}-unifying-receiver.rules

%files
%doc COPYING
%{udev_rules_dir}

%changelog
%autochangelog
