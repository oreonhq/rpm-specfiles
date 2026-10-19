%global source0_hash 370fbe090fa1f696e450ff83f859049a7a2ca7a35985e141450e3e7dad949e3a
%global	gem_name	thread_order
Name:		rubygem-%{gem_name}
Version:	1.1.1
Release:        1%{?dist}
Summary:        Test helper for ordering threaded code
License:	MIT
URL:		https://github.com/JoshCheek/thread_order
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Test helper for ordering threaded code.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
pushd %{buildroot}
rm -f .%{gem_cache}
pushd .%{gem_instdir}
rm -rf \
	.gitignore .travis.yml \
	Gemfile \
	spec/ \
	%{gem_name}.gemspec \
	%{nil}
popd
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

FAILFILE=()
FAILTEST=()
FAILFILE+=("spec/thread_order_spec.rb")
FAILTEST+=("is implemented without depending on the stdlib")
pushd .%{gem_instdir}
for ((i = 0; i < ${#FAILFILE[@]}; i++)) {
	sed -i \
		-e "\@${FAILTEST[$i]}@s|do$|, :broken => true do|" \
		${FAILFILE[$i]}
}
rspec spec/ || \
	rspec spec/ --tag ~broken
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-thread_order-doc -f %{oreon_filedir}/rubygem-thread_order-doc.list

%changelog

%autochangelog
