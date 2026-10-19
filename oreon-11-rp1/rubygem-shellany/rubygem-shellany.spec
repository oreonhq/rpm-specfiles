%global source0_hash 0e127a9132698766d7e752e82cdac8250b6adbd09e6c0a7fbbb6f61964fedee7
%global gem_name shellany
%global use_tests 1
Name:           rubygem-%{gem_name}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Simple, somewhat portable command capturing
License:        MIT
URL:            https://github.com/guard/shellany
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:      noarch
%if 0%{?use_tests}
%endif
# oreon:deps
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
MRI+JRuby compatible command output capturing.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
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

%if 0%{?use_tests}
pushd .%{gem_instdir}
rspec -Ilib --require shellany spec
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-shellany-doc -f %{oreon_filedir}/rubygem-shellany-doc.list

%changelog

%autochangelog
