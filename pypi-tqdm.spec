#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF8878F56397EFC71 (tqdm@cdcl.ml)
#
Name     : pypi-tqdm
Version  : 4.64.1
Release  : 124
URL      : https://files.pythonhosted.org/packages/c1/c2/d8a40e5363fb01806870e444fc1d066282743292ff32a9da54af51ce36a2/tqdm-4.64.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c1/c2/d8a40e5363fb01806870e444fc1d066282743292ff32a9da54af51ce36a2/tqdm-4.64.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/c1/c2/d8a40e5363fb01806870e444fc1d066282743292ff32a9da54af51ce36a2/tqdm-4.64.1.tar.gz.asc
Summary  : Fast, Extensible Progress Meter
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: pypi-tqdm-bin = %{version}-%{release}
Requires: pypi-tqdm-license = %{version}-%{release}
Requires: pypi-tqdm-python = %{version}-%{release}
Requires: pypi-tqdm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(colorama)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)

%description
|Logo|
tqdm
====
|Py-Versions| |Versions| |Conda-Forge-Status| |Docker| |Snapcraft|

%package bin
Summary: bin components for the pypi-tqdm package.
Group: Binaries
Requires: pypi-tqdm-license = %{version}-%{release}

%description bin
bin components for the pypi-tqdm package.


%package license
Summary: license components for the pypi-tqdm package.
Group: Default

%description license
license components for the pypi-tqdm package.


%package python
Summary: python components for the pypi-tqdm package.
Group: Default
Requires: pypi-tqdm-python3 = %{version}-%{release}

%description python
python components for the pypi-tqdm package.


%package python3
Summary: python3 components for the pypi-tqdm package.
Group: Default
Requires: python3-core
Provides: pypi(tqdm)
Requires: pypi(colorama)

%description python3
python3 components for the pypi-tqdm package.


%prep
%setup -q -n tqdm-4.64.1
cd %{_builddir}/tqdm-4.64.1
pushd ..
cp -a tqdm-4.64.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662312260
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tqdm
cp %{_builddir}/tqdm-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/pypi-tqdm/d710b33bdae7b273ee64376f2e7c722e098079e9 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tqdm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tqdm/d710b33bdae7b273ee64376f2e7c722e098079e9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
