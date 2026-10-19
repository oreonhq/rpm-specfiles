%global source0_hash 5408253274e33d9d27d4a98c46d2998266fd51cba58a7eb9d08f50e57ed23592
%global gem_name ansi
%global enable_checks 0
Name: rubygem-%{gem_name}
Version: 1.5.0
Release:        1%{?dist}
Summary:        ANSI at your fingertips!
License: LicenseRef-Callaway-BSD
URL: http://rubyworks.github.com/ansi
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?el6}
Requires:      ruby(abi) = 1.8
Requires:      rubygems
%endif
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Requires:      ruby(release)
Requires:      rubygems
%endif
%if 0%{?enable_checks}
%endif
BuildArch: noarch
%if 0%{?fc19} || 0%{?fc20} || 0%{?el6} || 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif
# oreon:deps
BuildRequires:  ruby
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The ANSI project is a superlative collection of ANSI escape code related
libraries enabling ANSI colorization and styling of 
console output. Byte for byte ANSI is the best ANSI code 
library available for the Ruby programming
language.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?enable_checks}
pushd .%{gem_instdir}
testrb -Ilib test
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ansi-doc -f %{oreon_filedir}/rubygem-ansi-doc.list

%changelog

%autochangelog
