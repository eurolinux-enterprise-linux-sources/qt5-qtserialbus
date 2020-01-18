%global qt_module qtserialbus

%define docs 1

Summary: Qt5 - SerialPort component
Name:    qt5-%{qt_module}
Version: 5.9.7
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
Source0: https://download.qt.io/official_releases/qt/5.9/%{version}/submodules/qtserialbus-opensource-src-%{version}.tar.xz

BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtserialport-devel >= %{version}

%description
Qt Serial Port provides the basic functionality, which includes configuring,
I/O operations, getting and setting the control signals of the RS-232 pinouts.

%if 0%{?docs}
%package doc
Summary: API documentation for %{name}
License: GFDL
Requires: %{name} = %{version}-%{release}
BuildRequires: qt5-qdoc
BuildRequires: qt5-qhelpgenerator
BuildArch: noarch
%description doc
%{summary}.
%endif

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%prep
%setup -q -n %{qt_module}-opensource-src-%{version}

%build
%{qmake_qt5} %{?_qt5_examplesdir:CONFIG+=qt_example_installs}

make %{?_smp_mflags}

%if 0%{?docs}
# HACK to avoid multilib conflicts in noarch content
# see also https://bugreports.qt-project.org/browse/QTBUG-42071
QT_HASH_SEED=0; export QT_HASH_SEED
make %{?_smp_mflags} docs
%endif

%install
make install INSTALL_ROOT=%{buildroot}

%if 0%{?docs}
make install_docs INSTALL_ROOT=%{buildroot}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.GPLv2 LICENSE.GPLv3 LICENSE.LGPLv3
%{_qt5_libdir}/libQt5SerialBus.so.5*
%{_qt5_bindir}/canbusutil
%{_qt5_plugindir}/canbus

%if 0%{?docs}
%files doc
%doc LICENSE.FDL
%{_qt5_docdir}/qtserialbus.qch
%{_qt5_docdir}/qtserialbus/
%endif

%files devel
%{_qt5_headerdir}/QtSerialBus/
%{_qt5_libdir}/libQt5SerialBus.so
%{_qt5_libdir}/libQt5SerialBus.prl
%dir %{_qt5_libdir}/cmake/Qt5SerialBus/
%{_qt5_libdir}/cmake/Qt5SerialBus
%{_qt5_libdir}/pkgconfig/Qt5SerialBus.pc
%{_qt5_prefix}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5SerialBus.la

# no examples, yet
%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif

%changelog
* Thu Feb 07 2019 Jan Grulich <jgrulich@redhat.com> - 5.9.7-1
- Update to 5.9.7
  Resolves: bz#1564014

* Fri Oct 06 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.2-1
- Update to 5.9.2
  Resolves: bz#1482806

* Thu Sep 21 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.1-1
- 5.9.1 - initial RHEL release
  Resolves: bz#1482806

* Wed May 31 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-1
- Upstream official release

* Fri May 26 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.1.rc
- Upstream Release Candidate retagged

* Wed May 24 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.rc.1
- Upstream Release Candidate 1

* Fri May 05 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.3
- New upstream beta3 release

* Sun Apr 16 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-0.beta.1
- New upstream beta release

* Wed Feb 01 2017 Helio Chissini de Castro <helio@kde.org> - 5.8.0-1
- New upstream version

* Sat Dec 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-2
- updated sources, drop pkgconfig-style deps (for now)

* Thu Nov 10 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.1-1
- New upstream version

* Tue Jul 05 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-1
- New Qt 5.7.0 package
