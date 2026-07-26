%global source0_hash 51d52d72a61729668ade581fe68fb10b9654027d2ac73203fbbcae73647b06b8

%global gem_name bacon

Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 24%{?dist}
Summary: A small RSpec clone
License: MIT
URL: http://github.com/chneukirchen/bacon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
%if 0%{?rhel} == 7
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Bacon is a small RSpec clone weighing less than 350 LoC but
nevertheless providing all essential features.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Derop weird non-utf8 characters in e-mail framework
LANG=C sed 's/\xc2//g' -i %{buildroot}%{gem_instdir}/ChangeLog

%check
pushd .%{gem_instdir}
bin/bacon -Ilib:. --automatic --quiet
popd

%files
%{_bindir}/bacon
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%dir %{gem_instdir}/bin
%{gem_instdir}/bin/bacon
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Rakefile
%{gem_instdir}/bacon.gemspec
%{gem_instdir}/test
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/RDOX
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/ChangeLog
%doc %{gem_docdir}

%changelog
%autochangelog
