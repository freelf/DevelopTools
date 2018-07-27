//
//  <#ClassName#>Controller.swift
//
//  Created by Beyond on 2018/6/6.
//  Copyright © 2018年 张东坡. All rights reserved.
//

import UIKit
import Moya
import Result
class <#ClassName#><#ListView#>DataSource: TCDataSource,TCDataSourceable {
    func reusableCellIdentifier(for indexPath: IndexPath) -> String {
        //这里返回对应 cell 的 reuseIdentifier，cell 需要遵守 TCReusableViewSupport 协议，实现对应方法。
        return ""
    }
}
class <#ClassName#><#ListView#>Delegate: TCDelegate {
    //需要引用当前 vc 的话声明一个 weak 的属性，比如：
    //weak var owner: <#ClassName#><#ListView#>Controller?
    //自己计算的 tableviewCell 高度，需要在这里返回
}
class <#ClassName#>ViewController: TWBaseViewController {
    //MARK: - Property
    var store: Store<<#ClassName#>Action, <#ClassName#>State, <#ClassName#>Command>!
    lazy var reducer = <#ClassName#>Reducer.init(owner: self)
    lazy var dataSource: <#ClassName#><#ListView#>DataSource = {
    return <#ClassName#><#ListView#>DataSource.init(<#listView#>: <#listView#>)
    }()
    lazy var delegate: <#ClassName#><#ListView#>Delegate = {
        return <#ClassName#><#ListView#>Delegate.init(<#listView#>: <#listView#>)
    }()
    // 习惯用代码的修改这个属性，然后自行创建对应的 ListView
    @IBOutlet weak var <#listView#>: UI<#ListView#>!
    //MARK: - Life Cycle
    override func viewDidLoad() {
        super.viewDidLoad()
        self.<#listView#>.dataSource = self.dataSource
        self.<#listView#>.delegate = self.delegate
        store = Store<<#ClassName#>Action, <#ClassName#>State, <#ClassName#>Command>(reducer: reducer.reducer, initialState: <#ClassName#>State())
        store.subscribe  { [weak self] state, previousState, command in
            self?.stateDidChange(state: state, previousState: previousState, command: command)
        }
    }
    //MARK: - State Change
    private func stateDidChange(state: <#ClassName#>State, previousState: <#ClassName#>State, command: <#ClassName#>Command?) {
        if let command = command {
            switch command {
                //解析command,比如网络请求，跳转，弹窗操作。
            }
            //根据 state 来改变 View 的状态，listView 需要如下调用：
            // let sectionData = TCSectionDataMetric.init(itemsData: state.collectionItems)
            // let globalData = TCGlobalDataMetric.init(sectionDataMetrics: [sectionData])
            //self.dataSource.globalDataMetric = globalData
            // self.tableView.reloadData()
            //listView的数据就是一个二维数组，[[rowItem]]
        }
    }
    //MARK: - Private Method
    
    //MARK: - Public Method
    
    //MARK: - Action Event

}

