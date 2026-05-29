%global source0_hash 370fbe090fa1f696e450ff83f859049a7a2ca7a35985e141450e3e7dad949e3a

%global	gem_name	thread_order

Name:		rubygem-%{gem_name}
Version:	1.1.1
Release:	15%{?dist}

Summary:	Test helper for ordering threaded code
License:	MIT
URL:		https://github.com/JoshCheek/thread_order
Source0:        https://rubygems.org/gems/thread_order-1.1.1.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(rspec) >= 3
BuildArch:	noarch

%description
Test helper for ordering threaded code.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%check
# The following test does not pass with using gem
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

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/License.txt
%doc	%{gem_instdir}/Readme.md

%{gem_libdir}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1-15
- Prepare for Oreon 11 (RP1)
