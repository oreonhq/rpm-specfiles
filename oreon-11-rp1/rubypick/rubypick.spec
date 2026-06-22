%global source0_hash a2e2036194e45f028feb96d3ca5d91bf5a2711d2da4de10b1cd2d2799c9bad5a

Name:           rubypick
Version:        1.1.1
Release:        1%{?dist}
Summary:        Stub to allow choosing Ruby runtime
License:        MIT
URL:            https://github.com/fedora-ruby/rubypick
Source0:        https://github.com/fedora-ruby/rubypick/archive/v%{version}.tar.gz#/rubypick-%{version}.tar.gz
BuildArch:      noarch

Requires:       ruby(runtime_executable)
Suggests:       ruby

%description
Fedora /usr/bin/ruby stub to allow choosing Ruby runtime. Similarly to rbenv
or RVM, it allows non-privileged user to choose which is preferred Ruby
runtime for current task.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n rubypick-%{version}

%install
mkdir -p %{buildroot}%{_bindir}
cp -a ruby %{buildroot}%{_bindir}

%files
%doc README.md LICENSE
%{_bindir}/ruby

%changelog
%autochangelog
